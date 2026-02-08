document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.querySelector("textarea[name='content']");
    if (textarea) {
        const editor = CodeMirror.fromTextArea(textarea, {
            mode: "htmlmixed",
            theme: "dracula",
            lineNumbers: true,
            lineWrapping: true,
            autoCloseTags: true,
            matchBrackets: true,
            indentUnit: 2,
            tabSize: 2,
            extraKeys: {
                "Tab": function(cm) {
                    if (cm.somethingSelected()) {
                        cm.indentSelection("add");
                    } else {
                        cm.replaceSelection("  ", "end");
                    }
                }
            }
        });
        
        editor.setSize("100%", "600px");
    }
});
