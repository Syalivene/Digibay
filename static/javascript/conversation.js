/*
<script>
            function refreshCodeBlock() {
                fetch('{% url "conversation:update-code-block" %}')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('my-code-block').innerHTML = data;
                });
            }
            setInterval(refreshCodeBlock, 2000);
        </script>

*/