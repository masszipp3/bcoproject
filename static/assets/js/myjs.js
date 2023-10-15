$(document).ready(function(){
    $('#cat').on('change',function(){
        cat_id=$(this).val()
        url = $(this).data('url')
        $('#subcat').empty()
        $('#subcat').append(`<option>Select an Sub Category</option>`)
        $.ajax({
            type: 'GET',
            url: url,
            data: {
              'catid': cat_id
            },
            success: function (response) {
              data = response.data
            //   console.log(data)
            for(category in data){
                $('#subcat').append("<option value='"+data[category].id+"'>"+data[category].name+'</option>');
            }
            },
            error: function (xhr, status, error) {
              console.error(xhr.responseText);
            }
          });
    })
})