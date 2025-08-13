<!-- contact.html -->
<form id="contact-form" method="post">
    {% csrf_token %}
        <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                        <label for="message">Message:</label>
                            <textarea id="message" name="message"></textarea>
                                <button type="submit">Submit</button>
                                </form>
                                
                                <script>
                                    const form = document.getElementById('contact-form');
                                        form.addEventListener('submit', (e) => {
                                                const name = document.getElementById('name').value.trim();
                                                        const email = document.getElementById('email').value.trim();
                                                                if (name === '' || email === '') {
                                                                            e.preventDefault();
                                                                                        alert('Please fill in both name and email fields.');
                                                                                                }
                                                                                                    });
                                                                                                    </script>
                                                                                                                                                                                                                           <label for=                                                                                                                                return render(request, 'menu.html', {'menu_items': menu_items})