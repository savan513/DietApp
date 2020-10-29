$("#Form-uname").blur(function(){
    username=$("#Form-uname").val();


    if(username.length > 0)
    {

        $.ajax('/checkusername', {

                type: 'GET',  // http method
                data: { uname:username  },  // data to submit

                success: function (msg) {
                    msg=JSON.parse(msg);
                    if(msg['is_available'])
                    {
                        swal("Oops..","This UserName is already taken","error");
                        $("#Form-uname").val(' ');

                    }
                },
                error: function (msg) {


                }
            });
    }
})

$("#Form-email").blur(function(){
    email=$("#Form-email").val();


    if(email.length > 0)
    {

        $.ajax('/checkemail', {

                type: 'GET',  // http method
                data: { email:email  },  // data to submit

                success: function (msg) {
                    msg=JSON.parse(msg);
                    if(msg['is_available'])
                    {
                        swal("Oops..","This Email is already taken","error");
                        $("#Form-email").val(' ');

                    }
                },
                error: function (msg) {


                }
            });
    }
})


$("#Form-pass").blur(function() {
        var password = $("#Form-pass").val();

        regx = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{4,}$/;
        if(password != "")
        {
            if (regx.test(password) == false )
            swal("Invalid Password\nPassword Must Contain \n1) At least One Capital Letter\n2) At least on Digit \n3) Small Letters")

        }
         })

    $("#Form-passc").blur(function() {
        var password = $("#Form-pass").val();
        var confpassword = $("#Form-passc").val();
        if (confpassword != password) {
            swal("Oops..","Password and Confirm Password are not matching","error")
        }
    })

function checksubmit() {
        var password = $("#Form-pass").val();

        regx = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{4,}$/;
        if (regx.test(password) == false)
          {  swal("Invalid Password\nPassword Must Contain \n1) At least One Capital Letter\n2) At least on Digit \n3) Small Letters")
            return false;
          }
        var confpassword = $("#Form-passc").val();
        if (confpassword != password) {
            swal("Oops..","Password and Confirm Password are not matching","error")
            return false;
        }
        if(!$("#tnc").is(':checked'))
        {
            swal("Oops..","Please Accept Term and Conditions by click on checkbox","error");
            return false;
        }

        return true;

}

