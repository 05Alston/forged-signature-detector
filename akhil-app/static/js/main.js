$(document).ready(function () {
    // Init
    // $('.img-preview1').hide();
    // $('.img-preview2').hide();
    // $('#btn-predict').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL1(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview1').css('background-image', 'url(' + e.target.result + ')');
                // $('#imagePreview1').hide();
                $('#imagePreview1').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    function readURL2(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview2').css('background-image', 'url(' + e.target.result + ')');
                // $('#imagePreview2').hide();
                $('#imagePreview2').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload1").change(function () {
        $('.image-preview1').show();
        // $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL1(this);
        if($(".img-preview1").is(":visible") && $(".img-preview2").is(":visible")){
            $('#btn-predict').show();
        }
    });
    $("#imageUpload2").change(function () {
        console.log('shit')
        $('.image-preview2').show();
        // $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL2(this);
        if($(".img-preview1").is(":visible") && $(".img-preview2").is(":visible")){
            $('#btn-predict').show();
        }
    });
    
    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        console.log(form_data)
        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });

});
