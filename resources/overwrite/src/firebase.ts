import { initializeApp } from 'firebase/app';
import { getFunctions, connectFunctionsEmulator } from 'firebase/functions';

// Update this to the actual config
const firebaseConfig = {
  apiKey: "AIzaSyD5dYIS2IThzWRC4a73erGk8_lLMCyn_C4",
  authDomain: "hitco-scaffold.firebaseapp.com",
  databaseURL: "https://hitco-scaffold-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "hitco-scaffold",
  storageBucket: "hitco-scaffold.appspot.com",
  messagingSenderId: "448658195585",
  appId: "1:448658195585:web:58131370b033ebf0383980",
  measurementId: "G-EV3X4CW9W9"
};

const app = initializeApp(firebaseConfig);
const functions = getFunctions(app);

if (process.env.NODE_ENV === 'local') {
  connectFunctionsEmulator(functions, 'localhost', 5001);
}

export { firebaseConfig, functions, app }