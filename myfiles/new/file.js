function inputFieldChange( )
{
   var b_val = document.getElementById("brok_er").value;
   if( b_val === "Add" )
   {
      document.getElementById("new_broker").style.display="inline";
   }
   else
   {
      document.getElementById("new_broker").style.display="none";
   }
}
