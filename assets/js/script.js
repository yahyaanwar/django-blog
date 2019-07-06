$(document).ready(function () {
    $('input[name="title"]').focusout(function () {
        var title = $(this).val()
        if( $(this).closest("#formBlogCreate").length )
        {
            if ($('input[name="slug"]').attr('edit') != 'true')
                $('input[name="slug"]').val(convertToSlug(title))
        }
    })

    $('input[name="slug"]').keypress(function () {
        var editable = $('input[name="slug"]').attr('edit')
        if( $(this).closest("#formBlogUpdate").length && editable != 'true')
        {
            showWarning({
                title: 'Update Slug',
                text: `Are you sure to update this slug`,
                confirm_text: 'Yes, update it!',
                cancel_text: 'No, cancel!',
                confirm: {
                    title: 'The Slug Editable',
                    text: `You can update the slug now`,
                    action() {
                        $('input[name="slug"]').attr('edit','true')
                    }
                },
                cancel: {
                    title: 'Cancelled',
                    text: 'The slug not able to update',
                    action() {
                        
                    }
                },
            });    
        }else if($(this).closest("#formBlogCreate").length){
            $(this).attr('edit', 'true')
        }
    })

    $('.btnDeletePost').click(function () {
        var title = $(this).attr('title')
        var url = $(this).attr('url')
        showWarning({
            title: 'Delete Post',
            text: `Are you sure to delete ${title}`,
            confirm_text: 'Yes, delete it!',
            cancel_text: 'No, cancel!',
            confirm: {
                title: 'Deleted!',
                text: `Your post with title ${title} has been deleted.`,
                action() {
                    window.location.replace(url);
                }
            },
            cancel: {
                title: 'Cancelled',
                text: 'Your post is safe :)',
                action() {

                }
            },
        });
    })
})

function convertToSlug(text) {
    return text
        .toLowerCase()
        .replace(/ /g, '-')
        .replace(/[^\w-]+/g, '');
}

function showWarning(vals) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger mr-3'
        },
        buttonsStyling: false,
    })

    swalWithBootstrapButtons.fire({
        title: vals.title || 'Warning',
        text: vals.text || 'Are you sure?',
        type: vals.type || 'warning',
        showCancelButton: true,
        confirmButtonText: vals.confirm_text || 'Yes, do it!',
        cancelButtonText: vals.cancel_text || 'No, cancel!',
        reverseButtons: true
    }).then((result) => {
        if (result.value) {
            vals.confirm.action && vals.confirm.action()
            swalWithBootstrapButtons.fire(
                vals.confirm.title || 'Done!',
                vals.confirm.text || '',
                vals.confirm.type || 'success'
            )
        } else if (result.dismiss === Swal.DismissReason.cancel) {
            vals.cancel.action && vals.cancel.action()
            swalWithBootstrapButtons.fire(
                vals.cancel.title || 'Cancelled',
                vals.cancel.text || '',
                vals.cancel.type || 'error'
            )
        }
    })
}