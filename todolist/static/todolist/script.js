// todolist/static/todolist/script.js
$(document).ready(function() {
    // Delete All To-Dos
    $("#delete-all").click(function() {
        $("#todo-list").empty();
    });

    // Delete Completed To-Dos
    $("#delete-completed").click(function() {
        $(".form-check").each(function() {
            if ($(this).find("input[type='checkbox']").is(":checked")) {
                $(this).remove();
            }
        });
    });
});
