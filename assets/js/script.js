$(document).ready(function(){
    $('input[name="title"]').focusout(function(){
        var title = $(this).val();
        if($('input[name="slug"]').attr('edit') != 'true')
            $('input[name="slug"]').val(convertToSlug(title))
    })

    $('input[name="slug"]').keypress(function(){
        $(this).attr('edit','true')
    })
})
s
function convertToSlug(text)
{
    return text
        .toLowerCase()
        .replace(/ /g,'-')
        .replace(/[^\w-]+/g,'')
        ;
}