// Send sats connecting to WEBLN and LNURLPAY

// grab the ln address from the html page, can we query directly from the database?
// this doesn't work, tbd
//const ln_address = document.getElementById("ln-address").value;

// initial payment to enable payments with Alby
async function pay() {
  //const comment = document.getElementById("message").value;

  // https://github.com/dolcalmi/lnurl-pay
  // can use a simple lnurl request invoice
  // pass in lnurl or ln address, how many sats you want to send, and if you want to send a comment
  const { invoice, params, successAction, validatePreimage } =
    await LnurlPay.requestInvoice({
      // this needs to grab the address of the creator from the database, or from the html page.. TBD
      lnUrlOrAddress: "subirachs@getalby.com",
      //lnUrlOrAddress: ln_address,
      tokens: 1,
      //comment: comment,
    });
  
  // call webln
  if (window.webln) {
    await webln.enable();

    // second call to send payment
    const payResponse = await webln.sendPayment(invoice);

    // get preimage from the wallet, we get the preimage from the wallet
    document.getElementById("preimage").innerHTML = payResponse.preimage;

    // validate the preimage by comparing the hash of the preimage to the payment hash of the lightning invoice
    // if it validates, then it confirms
    if (validatePreimage(payResponse.preimage)) {
      document.getElementById("connect_success").innerHTML = "1 SAT has been sent to initialize connection! Sending sats is now enabled.";
    } else {
      alert("fail");
    }
  } else {
    alert("NO webln enabled");
  }
}

document.getElementById("unlock-button").addEventListener("click", (event) => {
  event.preventDefault();
  event.target.innerHTML = "loading...";
  pay();
  //event.target.innerHTML = "Boost Mode..."
});

// 1 SAT
async function pay_1_sat() {

  // https://github.com/dolcalmi/lnurl-pay
  // can use a simple lnurl request invoice
  // pass in lnurl or ln address, how many sats you want to send, and if you want to send a comment
  const { invoice, params, successAction, validatePreimage } =
    await LnurlPay.requestInvoice({
      // this needs to grab the address of the creator from the database, TBD
      lnUrlOrAddress: "subirachs@getalby.com",
      tokens: 1,
    });
  
  // call webln
  if (window.webln) {
    await webln.enable();

    // second call to send payment
    const payResponse = await webln.sendPayment(invoice);

    // get preimage from the wallet, we get the preimage from the wallet
    document.getElementById("preimage").innerHTML = payResponse.preimage;

    // validate the preimage by comparing the hash of the preimage to the payment hash of the lightning invoice
    // if it validates, then it confirms
    if (validatePreimage(payResponse.preimage)) {
      document.getElementById("success").innerHTML = " BOOSTED 1 SAT! "; 
    } else {
      alert("fail");
    }
  } else {
    alert("NO webln enabled");
  }
}

document.getElementById("one-sat-button").addEventListener("click", (event) => {
  event.preventDefault();
  //event.target.innerHTML = "BOOSTED!";
  pay_1_sat();
});

// 5 SATS
async function pay_five_sats() {

  // https://github.com/dolcalmi/lnurl-pay
  // can use a simple lnurl request invoice
  // pass in lnurl or ln address, how many sats you want to send, and if you want to send a comment
  const { invoice, params, successAction, validatePreimage } =
    await LnurlPay.requestInvoice({
      // this needs to grab the address of the creator from the database, TBD
      lnUrlOrAddress: "subirachs@getalby.com",
      tokens: 5,
    });
  
  // call webln
  if (window.webln) {
    await webln.enable();

    // second call to send payment
    const payResponse = await webln.sendPayment(invoice);

    // get preimage from the wallet, we get the preimage from the wallet
    document.getElementById("preimage").innerHTML = payResponse.preimage;

    // validate the preimage by comparing the hash of the preimage to the payment hash of the lightning invoice
    // if it validates, then it confirms
    if (validatePreimage(payResponse.preimage)) {
      document.getElementById("success").innerHTML = " BOOSTED 5 SATS! ";
    } else {
      alert("fail");
    }
  } else {
    alert("NO webln enabled");
  }
}

document.getElementById("five-sats-button").addEventListener("click", (event) => {
  event.preventDefault();
  //event.target.innerHTML = "BOOSTED!";
  pay_five_sats();
});

// 10 SATS
async function pay_ten_sats() {

  // https://github.com/dolcalmi/lnurl-pay
  // can use a simple lnurl request invoice
  // pass in lnurl or ln address, how many sats you want to send, and if you want to send a comment
  const { invoice, params, successAction, validatePreimage } =
    await LnurlPay.requestInvoice({
      // this needs to grab the address of the poster from the database
      // not sure how to do this yet
      lnUrlOrAddress: "subirachs@getalby.com",
      tokens: 10,
    });
  
  // call webln
  if (window.webln) {
    await webln.enable();

    // second call to send payment
    const payResponse = await webln.sendPayment(invoice);

    // get preimage from the wallet, we get the preimage from the wallet
    document.getElementById("preimage").innerHTML = payResponse.preimage;

    // validate the preimage by comparing the hash of the preimage to the payment hash of the lightning invoice
    // if it validates, then it confirms
    if (validatePreimage(payResponse.preimage)) {
      document.getElementById("success").innerHTML = " BOOSTED 10 SATS! ";
    } else {
      alert("fail");
    }
  } else {
    alert("NO webln enabled");
  }
}

document.getElementById("ten-sats-button").addEventListener("click", (event) => {
  event.preventDefault();
  //event.target.innerHTML = "BOOSTED!";
  pay_ten_sats();
});

// CUSTOM SATS
async function pay_custom_sats() {
  const custom_amount = document.getElementById("custom-amount").value;

  // https://github.com/dolcalmi/lnurl-pay
  // can use a simple lnurl request invoice
  // pass in lnurl or ln address, how many sats you want to send, and if you want to send a comment
  const { invoice, params, successAction, validatePreimage } =
    await LnurlPay.requestInvoice({
      // this needs to grab the address of the creator from the database, TBD
      lnUrlOrAddress: "subirachs@getalby.com",
      tokens: custom_amount,
    });
  
  // call webln
  if (window.webln) {
    await webln.enable();

    // second call to send payment
    const payResponse = await webln.sendPayment(invoice);

    // get preimage from the wallet, we get the preimage from the wallet
    document.getElementById("preimage").innerHTML = payResponse.preimage;

    // validate the preimage by comparing the hash of the preimage to the payment hash of the lightning invoice
    // if it validates, then it confirms
    if (validatePreimage(payResponse.preimage)) {
      document.getElementById("success").innerHTML = " BOOSTED " + custom_amount + " SATS!"; 
    } else {
      alert("fail");
    }
  } else {
    alert("NO webln enabled");
  }
}

document.getElementById("custom-sats-button").addEventListener("click", (event) => {
  event.preventDefault();
  //event.target.innerHTML = "BOOSTED!";
  pay_custom_sats();
});





// stream function TBD

//function stream() {
//  pay();
//  window.setInterval(pay, 10000); // TODO: make this smarter. e.g. with some debouncing
//}
//
//document.getElementById("stream-button").addEventListener("click", (event) => {
//  event.preventDefault();
//  event.target.innerHTML = "streaming...";
//  stream();
//});


// testing
