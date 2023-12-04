function getStory() {
    const storyLength = $('#storyLength').val();
    const storyType = $('#storyType').val();

    // Show the spinner
    $('#loadingSpinner').show();

    // Include the dropdown values in the GET request as query parameters
    $.get(`/gen_lib?length=${storyLength}&type=${storyType}`, function(data) {
        $('#storyArea').val(data.story);
        adjustTextareaHeight('storyArea');
    
        // Send the story to get the fillable items
        $.post('/list_fills', { story: data.story }, function(fillData) {
            // Create textboxes for each fillable item
            let fillInputs = '<div class="mt-3">';
            for (let fill of fillData.fills) {
                fillInputs += `
                    <div class="input-group mb-2">
                        <input type="text" class="form-control fill-input" placeholder="${fill}" data-fill="${fill}">
                        <button class="btn btn-primary enter-btn" style="display:none;">Enter</button>
                        <button class="btn btn-secondary autofill-btn" style="display:none;" onclick="autoFillWord('${fill}')">AutoFill</button>
                    </div>`;
            }
            fillInputs += '</div>';
        
            // Insert the textboxes between the buttons/dropdowns and the story textarea
            $('#storyArea').before(fillInputs);
        });
    
    }).always(function() {
        // Hide the spinner once the request is complete
        $('#loadingSpinner').hide();
    });
}


function autofill(fillable) {
    // Post request to autofill a specific fillable item
    $.post('/list_fills', { story: data.story }, function(fillData) {
        if (fillData.list && Array.isArray(fillData.list)) {
            let fillInputs = '<div class="mt-3">';
            fillData.list.forEach(function(fill) {
                fillInputs += `
                    <div class="input-group mb-2">
                        <input type="text" class="form-control fill-input" placeholder="${fill}" data-fill="${fill}">
                        <button class="btn btn-primary enter-btn" style="display:none;">Enter</button>
                        <button class="btn btn-secondary autofill-btn" style="display:none;" onclick="autoFillWord('${fill}')">AutoFill</button>
                    </div>`;
            });
            fillInputs += '</div>';
            $('#storyArea').before(fillInputs);
        } else {
            console.error('fillData.list is undefined or not an array', fillData);
        }
    });
}
function adjustTextareaHeight(textareaId) {
    const textarea = document.getElementById(textareaId);
    const lines = textarea.value.split('\n').length;
    textarea.rows = Math.max(lines, 1);  // Ensure at least 1 row
}

function autoFillWord(index, label) {
    const prompt = `Please provide a ${label}`;

    $.post('/auto_gen_word', { prompt: prompt }, function(data) {
        // Assuming the endpoint returns the generated word in a 'word' property
        const word = data.word;
        
        // Populate the corresponding input field with the generated word
        $(`#fillable${index}`).val(word);
    })
    .fail(function() {
        alert("Error occurred while trying to autofill the word. Please try again.");
    });
}

function gen_link() {
    // create a unique html doc of the story for social media / html
    // save to azure file storage for static linking
    const textarea = document.getElementById(textareaId);
    const lines = textarea.value.split('\n').length;
    textarea.rows = Math.max(lines, 1);  // Ensure at least 1 row
}
