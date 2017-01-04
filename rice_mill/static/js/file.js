function inputFieldChange( )
{
   var b_val = document.getElementById("broker").value;
   if( b_val === "Add" )
   {
      document.getElementById("new_broker").style.display="inline";
      document.getElementById("new_broker").required = true;
   }
   else
   {
      document.getElementById("new_broker").style.display="none";
      document.getElementById("new_broker").required = false;
      //alert(document.getElementById("new_broker").required+"HELLO");
   }
}

function calculateTotal()
{
   var b_val = document.getElementById("qty").value;
   //alert(b_val);
   /*
      if( b_val === "Add" )
      {
      document.getElementById("new_broker").style.display="inline";
      }
      else
      {
      document.getElementById("new_broker").style.display="none";
      }
    */
}

function displayForm() 
{
   var x = document.getElementByName('form_type').submit();
   //alert( "myurl:"+x );
   
   /*
   var radios = document.getElementsByName('formselector');
   var form_type = 1;
   for( var i = 0, length = radios.length; i < length; i++ )
   {
      if( radios[i].checked )
      {
         // do whatever you want with the checked radio
         //alert( "Hello"+radios[i].value);
         form_type = radios[i].value;
         break;
      }
   }
   //document.form_type.action = document.form_type.action+form_type;
   var myurl = document.form_type.action;
   //alert( "myurl:" );
   alert( "myurl:"+myurl+form_type );
   //document.getElementsByName('formselector').submit();

   //alert( document.myform.action+"/"+form_type );
   */
}
