document.addEventListener('DOMContentLoaded', function () {
        const messages = document.querySelectorAll('.message');

        messages.forEach(function (message) {

            message.style.opacity = 1;

            setTimeout(function () {
                message.style.opacity = 0;

                setTimeout(function () {
                    message.style.maxHeight = '0';
                }, 300);
            }, 5000);
        });
    });

