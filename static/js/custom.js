var deleted_id = '';
var update_id = "";

function open_create($this){
    $('#id_create_student').show();
    $('#edit_click').hide();
    $('#add_more_student').prop('disabled', true);
    $('#edit_more_student').prop('disabled', true);
    $('#delete_more_student').prop('disabled', true);
    $('#get_more_student').prop('disabled', true);
    document.getElementById("id_response").innerHTML = "";
}

function open_get($this){
    $('#id_get_student').show();
    $('#add_more_student').prop('disabled', true);
    $('#edit_more_student').prop('disabled', true);
    $('#delete_more_student').prop('disabled', true);
    $('#get_more_student').prop('disabled', true);
    document.getElementById("id_response").innerHTML = "";
}

function open_delete($this){
    $('#id_delete_student').show();
    $('#add_more_student').prop('disabled', true);
    $('#edit_more_student').prop('disabled', true);
    $('#delete_more_student').prop('disabled', true);
    $('#get_more_student').prop('disabled', true);
    document.getElementById("id_response").innerHTML = "";
}

function open_edit($this){
    $('#id_edit_student').show();
    $('#add_more_student').prop('disabled', true);
    $('#edit_more_student').prop('disabled', true);
    $('#delete_more_student').prop('disabled', true);
    $('#get_more_student').prop('disabled', true);
    document.getElementById("id_response").innerHTML = "";
}

function actual_edit($this){
    $('#id_actual_edit_student').show();
    $('#add_more_student').prop('disabled', true);
    $('#edit_more_student').prop('disabled', true);
    $('#delete_more_student').prop('disabled', true);
    $('#get_more_student').prop('disabled', true);
    document.getElementById("id_response").innerHTML = "";
}

function save_student($this){
    $.ajax({
        url: $this.attr('action'),
        type: $this.attr('method'),
        data: $this.serialize(),
        datatype: JSON,
        success: function(response){

            response = JSON.parse(response);

            if(response.status){
                event.preventDefault();
                $('#id_response').append(JSON.stringify(response,null,2));
                $('#id_added_students').append(response.student);
                $('#id_create_student').hide();
                $('#add_more_student').prop('disabled', false);
                $('#edit_more_student').prop('disabled', false);
                $('#delete_more_student').prop('disabled', false);
                $('#get_more_student').prop('disabled', false);
                $('#add_more_student').attr('onclick', 'open_create()');
                $('#id_create_student').hide();
                $("#id_create_student")[0].reset();
            }else{
                $('#id_response').append(JSON.stringify(response,null,2));
            }
        }
    });
    return false;
}

function edit_save_student($this){
    $.ajax({
        url: $this.attr('action'),
        type: $this.attr('method'),
        data: $this.serialize(),
        datatype: JSON,
        success: function(response){

            response = JSON.parse(response);

            if(response.status){
                event.preventDefault();
                $('#id_first_name').val(response.user_info.first_name);
                $('#id_response').append(JSON.stringify(response,null,2));
                $('#id_added_students').append(response.student);
                $('#id_create_student').hide();
                $('#add_more_student').prop('disabled', false);
                $('#edit_more_student').prop('disabled', false);
                $('#delete_more_student').prop('disabled', false);
                $('#get_more_student').prop('disabled', false);
                $('#add_more_student').attr('onclick', 'open_create()');
                $('#id_create_student').hide();
                $("#id_create_student")[0].reset();
            }else{
                $('#id_response').append(JSON.stringify(response,null,2));
                $("#id_create_student")[0].reset();
                
            }
        }
    });
    return false;
}


function remove_student($this){
    $.ajax({
        url: $this.attr('action'),
        type: $this.attr('method'),
        data: $this.serialize(),
        datatype: JSON,
        success: function(response){

            response = JSON.parse(response);


            if(response.status){
                debugger;
                event.preventDefault();
                deleted_id = response.student_deleted.id;
                $('#id_response').append(JSON.stringify(response,null,2));
                $("#id_student_"+deleted_id).remove();
                $('#id_delete_student').hide();
                $('#add_more_student').prop('disabled', false);
                $('#edit_more_student').prop('disabled', false);
                $('#delete_more_student').prop('disabled', false);
                $('#get_more_student').prop('disabled', false);
                $('#add_more_student').attr('onclick', 'open_create()');
                $('#id_create_student').hide();
                $("#id_delete_student")[0].reset();
            }else{
                $('#id_response').append(JSON.stringify(response,null,2));
                $("#id_delete_student")[0].reset();
                
            }
        }
    });
    return false;
}

function fetch_student($this){
    $.ajax({
        url: $this.attr('action'),
        type: $this.attr('method'),
        data: $this.serialize(),
        datatype: JSON,
        success: function(response){

            response = JSON.parse(response);

            if(response.status){
                event.preventDefault();
                $('#id_response').append(JSON.stringify(response,null,2));
                $('#id_get_student').hide();
                $('#add_more_student').prop('disabled', false);
                $('#edit_more_student').prop('disabled', false);
                $('#delete_more_student').prop('disabled', false);
                $('#get_more_student').prop('disabled', false);
                $('#get_more_student').attr('onclick', 'open_get()');
                $("#id_get_student")[0].reset();
            }else{
                $('#id_response').append(JSON.stringify(response,null,2));
                
            }
        }
    });
    return false;
}

function update_student($this){
    $.ajax({
        url: $this.attr('action'),
        type: $this.attr('method'),
        data: $this.serialize(),
        datatype: JSON,
        success: function(response){

            response = JSON.parse(response);

            if(response.status){
                debugger;
                event.preventDefault();
                $('#id_create_student').show();
                $('#id_first_name').val(response.user_info.first_name);
                $('#id_last_name').val(response.user_info.last_name);
                $('#id_email').val(response.user_info.email);
                $('#id_nationality').val(response.student.nationality);
                $('#id_response').append(JSON.stringify(response,null,2));
                $('#id_edit_student').hide();
                $('#add_more_student').prop('disabled', false);
                $('#edit_more_student').prop('disabled', false);
                $('#delete_more_student').prop('disabled', false);
                $('#get_more_student').prop('disabled', false);
                $('#get_more_student').attr('onclick', 'open_edit()');
                $("#id_edit_student")[0].reset();
            }else{
                $('#id_response').append(JSON.stringify(response,null,2));
                
            }
        }
    });
    return false;
}

function remove_form($this) {
    $('#id_create_student').hide();
    $('#id_get_student').hide();
    $('#id_delete_student').hide();
    $('#id_edit_student').hide();
    $('#id_update_student').hide();
    $('#add_more_student').prop('disabled', false);
    $('#edit_more_student').prop('disabled', false);
    $('#delete_more_student').prop('disabled', false);
    $('#get_more_student').prop('disabled', false);
    $("#id_create_student")[0].reset();
    $("#id_create_student")[0].reset();
    $("#id_delete_student")[0].reset();
    $("#id_get_student")[0].reset();
    $("#id_edit_student")[0].reset();
    document.getElementById("id_response").innerHTML = "";
}