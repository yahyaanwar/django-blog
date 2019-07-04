$(document).ready(function () {
    $('input[name="title"]').focusout(function () {
        var title = $(this).val()
        if ($('input[name="slug"]').attr('edit') != 'true')
            $('input[name="slug"]').val(convertToSlug(title))
    })

    $('input[name="slug"]').keypress(function () {
        $(this).attr('edit', 'true')
    })

    $('.btnDeletePost').click(function () {
        var title = $(this).attr('title')
        var url = $(this).attr('url')
        if (confirm('Apakah anda yakin akan menghapus Post '+title+'?')) {
            window.location.replace(url)
        }
    })
})

function convertToSlug(text) {
    return text
        .toLowerCase()
        .replace(/ /g, '-')
        .replace(/[^\w-]+/g, '');
}