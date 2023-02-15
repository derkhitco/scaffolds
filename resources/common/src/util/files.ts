import { firebaseApp } from "./../firebase";
import { getStorage, ref as storRef, getDownloadURL, uploadBytes } from "firebase/storage";
import { FileObject } from "./types";

const storage = getStorage(firebaseApp);

export async function reloadStorageRefs(obj: any, outer = true, promises: Promise<any>[] = []) {
    // If it is not an object, there will be no uploadables
    if (typeof obj !== 'object') { return obj }

    // If it is an Object, we need to iterate over it
    for (const key in obj) {
        // If the item is a file reference, we need to reload it
        if (obj[key].path && obj[key].filetype) {
            promises.push(refreshFileUrl(obj[key], promises).then((fileObj) => { obj[key] = fileObj }))
        }
        // If the item is an object, we need to recurse
        promises.push(reloadStorageRefs(obj[key], false, promises).then((newObj) => { obj[key] = newObj }))
    }
    if (outer) {
        await Promise.all(promises)
    }
    return obj

}

export function cleanEmptyRefs(obj: any) {
    // If it is not an object, there will be no uploadables    
    if (typeof obj !== 'object') { return obj }
    // Iteratie over the object keys
    for (const key in obj) {
        // If it is empty, remove it else recurse
        if (obj[key] === null || obj[key] === undefined) {
            delete obj[key]
        } else {
            obj[key] = cleanEmptyRefs(obj[key])
        }
    }
    return obj
}

export async function uploadFiles(obj: any, path: string) {
    // If it is not an object, there will be no uploadables
    if (typeof obj !== 'object') { return obj }

    // If it is an array, we need to iterate over it
    for (const key in obj) {
        // If the item is a file, we need to upload it
        if (obj[key]?.file && obj[key].file instanceof File) {
            obj[key] = await uploadFile(obj[key], `${path}/${key}`)
        }

        // If the item is a reference to a file, we need to normalize it
        if (obj[key]?.path && obj[key].filetype && !obj[key].url) {
            obj[key] = { path: obj[key].path, filetype: obj[key].filetype }
        }

        // If the item is an object, we need to recurse
        obj[key] = await uploadFiles(obj[key], `${path}/${key}`)
    }
    // Return the result
    return obj
}


async function uploadFile(fileObj: FileObject, path: string): Promise<FileObject> {
    if (!fileObj.file) { return fileObj }
    const key = `${path}/${fileObj.file.name}`
    const fileRef = storRef(storage, key);
    await uploadBytes(fileRef, await fileObj.file);
    return { path: key, filetype: fileObj.file.type }
}



async function refreshFileUrl(fileObj: FileObject, promises: Promise<any>[]): Promise<FileObject> {
    const pathReference = storRef(storage, fileObj.path);
    promises.push(getDownloadURL(pathReference).then((url) => { fileObj.url = url }))
    return fileObj
}