
document.addEventListener("DOMContentLoaded", function () {

    // Increase quantity
    document.querySelectorAll(".increase").forEach(button => {

        button.addEventListener("click", function () {

            const form = this.closest(".quantity-form");
            const input = form.querySelector(".quantity-input");

            const currentValue = parseInt(input.value) || 0;
            const maxValue = parseInt(input.max);

            if (currentValue < maxValue) {
                input.value = currentValue + 1;
            } else {
                alert("You cannot add more than the available stock.");
            }

        });

    });


    // Decrease quantity
    document.querySelectorAll(".decrease").forEach(button => {

        button.addEventListener("click", function () {

            const form = this.closest(".quantity-form");
            const input = form.querySelector(".quantity-input");

            const currentValue = parseInt(input.value) || 0;

            if (currentValue > 0) {
                input.value = currentValue - 1;
            }

        });

    });


    // Validate quantity before submitting
    document.querySelectorAll(".quantity-form").forEach(form => {

        form.addEventListener("submit", function (event) {

            const input = this.querySelector(".quantity-input");

            const quantity = parseInt(input.value);
            const maxStock = parseInt(input.max);

            if (
                isNaN(quantity) ||
                quantity < 0 ||
                quantity > maxStock
            ) {
                event.preventDefault();

                alert(
                    "Please enter a quantity between 0 and " +
                    maxStock + "."
                );
            }

        });

    });

});
