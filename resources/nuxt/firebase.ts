import { initializeApp } from 'firebase/app';
import { getFunctions, connectFunctionsEmulator } from 'firebase/functions';

// Update this to the actual config
const firebaseConfig = {%FBCONFIG%};

const firebaseApp = initializeApp(firebaseConfig);
// const app = initializeApp(firebaseConfig);
const functions = getFunctions(firebaseApp);

if (process.env.NODE_ENV === 'local') {
  connectFunctionsEmulator(functions, 'localhost', 5001);
}



export { functions, firebaseApp }