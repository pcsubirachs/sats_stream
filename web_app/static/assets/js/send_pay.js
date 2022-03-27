async function pay() {
  //const comment = document.getElementById("message").value;
  const { invoice, params, successAction, validatePreimage } =
    await LnurlPay.requestInvoice({
      lnUrlOrAddress: "ben@lnurl.com",
      tokens: 1,
      //comment: comment,
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

document.getElementById("unlock-button").addEventListener("click", (event) => {
  event.preventDefault();
  event.target.innerHTML = "loading...";
  pay();
});
