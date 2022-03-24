async function pay() {
  const comment = document.getElementById("message").value;

  // https://github.com/dolcalmi/lnurl-pay
  // can use a simple lnurl request invoice
  // filling out address, how many sats you want to send, and if you want to send a comment
  const { invoice, params, successAction, validatePreimage } =
    await LnurlPay.requestInvoice({
      // this needs to grab the address of the poster from the database
      // not sure how to do this yet
      lnUrlOrAddress: "subirachs@getalby.com",
      tokens: 10,
      comment: comment,
    });

  if (window.webln) {
    await webln.enable();

    const payResponse = await webln.sendPayment(invoice);

    document.getElementById("preimage").innerHTML = payResponse.preimage;

    if (validatePreimage(payResponse.preimage)) {
      document.getElementById("success").append("yay, paid -- ");
    } else {
      alert("fail");
    }
  } else {
    alert("NO webln enabled");
  }
}

function stream() {
  pay();
  window.setInterval(pay, 10000); // TODO: make this smarter. e.g. with some debouncing
}

document.getElementById("unlock-button").addEventListener("click", (event) => {
  event.preventDefault();
  event.target.innerHTML = "loading...";
  pay();
});

document.getElementById("stream-button").addEventListener("click", (event) => {
  event.preventDefault();
  event.target.innerHTML = "streaming...";
  stream();
});
