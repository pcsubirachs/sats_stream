import { requestProvider } from 'webln';

try {
  const webln = await requestProvider();
  // Now you can call all of the webln.* methods
}
catch(err) {
  // Tell the user what went wrong
  alert(err.message);
}