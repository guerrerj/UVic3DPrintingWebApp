// Get Stripe publishable key
var baseurl = window.location.origin;
var stripe = {};
fetch(baseurl + "/payments/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  stripe = Stripe(data.publicKey);

  // Event handler
  document.querySelectorAll("#submitPaymentBtn").forEach(item => { 
          item.addEventListener("click", onClickEvent);
      })
  });

  function onClickEvent(e){
    try{
        // Get Checkout Session ID
        // Get jobId value 
       var jobId = e.target.value;
      
        fetch(baseurl+"/payments/create-checkout-session/" + jobId)
        .then((result) => { return result.json(); })
        .then((data) => {      
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({sessionId: data.sessionId})
        })
        .then((res) => {
          console.log(res);
        });
    }catch(error){
      console.log(error);
    }
  }