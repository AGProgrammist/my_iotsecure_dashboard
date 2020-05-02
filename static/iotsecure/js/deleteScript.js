$("form").on('click', function (event) {
    event.preventDefault();
    var id = $(this).attr("id");
    if ($("#delete_btn_" + id).is(":disabled") == false) {
        $.confirm({
            title: 'Устгах',
            type: 'red',
            content: 'Та итгэлтэй байна уу?',
            typeAnimated: true,
            buttons: {
                Тийм: {
                    text: 'Тийм',
                    btnClass: 'btn-red',
                    action: function () {
                        $("#" + id).submit()
                    }
                },
                Үгүй: {

                }
            }
        });
    }
})
