$(function(){
    $('#confirmpayModal').on('shown.bs.modal', function (event) {
        $('#confirmpaypwd').val('');
	    $('#confirmpaypwd').focus();
	});
});

function confirm_pay(formid) {
    paypwd = $('#confirmpaypwd').val();
    $.post("/directsale/confirmpay/", {"paypwd":paypwd}, function(data){
        if(data.result){
            $('#confirmpayModal').modal('hide');
            $('#'+formid).submit();
        } else {
            $('#confirmpaypwd').focus();
            $('#confirmpaypwd').popover('show');
        }
        },"json");
}