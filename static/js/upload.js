const progress = document.getElementById('progress')
const progress_wrapper = document.getElementById('progress_wrapper')
const progress_status = document.getElementById('progress_status')

const upload_btn = document.getElementById('upload_btn')
const loading_btn = document.getElementById('loading_btn')
const cancel_btn = document.getElementById('cancel_btn')

const alert_wrapper = document.getElementById('alert_wrapper')

const uploadform = document.getElementById('upload-form')
const input = document.getElementById('file_input')
const input_label = document.getElementById('file_input_label')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

function show_alert(message, alert) {

    alert_wrapper.innerHTML = `
         <div id="alert" class="alert alert-${alert} alert-dismissible fade show" role="alert">
             <span>${message}</span>
             <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                 <span aria-hidden="true">&times;</span>
             </button>
         </div>
     `;

};

function input_filename() {
    input_label.innerText = input.files[0].name;
}

function upload() {
    if (!input.value) {
        show_alert("No file Selected", "warning")
        return;
    }

    alert_wrapper.innerHTML = "";
    input.disabled = true;
    upload_btn.classList.add("d-none");
    loading_btn.classList.remove("d-none");
    cancel_btn.classList.remove("d-none");
    progress_wrapper.classList.remove("d-none");

    const input_file = input.files[0]

    const formdata = new FormData()
    formdata.append('csrfmiddlewaretoken', csrf[0].value)
    formdata.append('input_data', input_file)

    $.ajax({
        type: 'POST',
        url: uploadform.action,
        enctype: 'multipart/form-data',
        data: formdata,
        beforeSend: function () {

        },
        xhr: function () {
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress', function (e) {
                if (e.lengthComputable) {
                    const loaded = e.loaded;
                    const total = e.total;
                    const percent_complete = (loaded / total) * 100;

                    progress.setAttribute("style", `width: ${Math.floor(percent_complete)}%`);
                    progress_status.innerText = `${Math.floor(percent_complete)}% uploaded`;
                }
            })

            cancel_btn.addEventListener('click', function () {
                xhr.abort()
                show_alert(`Upload cancelled`, "warning");
                reset();
            })
            return xhr
        },
        success: function (response) {
            show_alert(`${response.message}`, "success");
            reset();
        },
        error: function (error) {
            show_alert(`Error uploading file`, "danger");
            reset();
        },
        cache: false,
        contentType: false,
        processData: false,
    });
}

function reset() {
    input.value = null;
    cancel_btn.classList.add("d-none");
    input.disabled = false;
    upload_btn.classList.remove("d-none");
    loading_btn.classList.add("d-none");
    progress_wrapper.classList.add("d-none");
    progress.setAttribute("style", `width: 0%`);
    input_label.innerText = "Select file - (csv only)";
}
