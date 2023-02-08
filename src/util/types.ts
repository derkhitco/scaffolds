
export type FileObject = {
    path: string,
    filetype: string,
    url?: string,
    file?: File
}

export type HomeTexts = {
    title: string,
    description: string,
    text: string,
    image?: FileObject
}

export type Texts = {
    home?: HomeTexts,
}
