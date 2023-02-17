
export type FileObject = {
    path: string,
    filetype: string,
    url?: string,
    file?: File
}

export type Home = {
    title: string,
    description: string,
    text: string,
    image?: FileObject
}

export type About = {
    title: string,
    description: string,
    text: string,
    image?: FileObject
}

export type Pages = {
    // pages type definition, do not remove this line
	home: Home,
    about: About
}

export type ConfigStatus = {
    cookiesStatus: boolean,
    localStorageStatus: boolean,
    trackingStatus: boolean,
    showModalStatus: boolean
}
