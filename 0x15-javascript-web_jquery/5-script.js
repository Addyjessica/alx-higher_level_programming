//Using jquery to change the color of the header
$(function () {
    $("DIV#add_item").on("click", function () {
        $("UL.my_list").append('<Li>' + 'Item' + '</Li>');
    });
});
