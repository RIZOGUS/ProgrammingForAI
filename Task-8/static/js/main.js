document.addEventListener('DOMContentLoaded', () => {
    // Tab Switching
    const tabs = document.querySelectorAll('.tab-btn');
    const panels = document.querySelectorAll('.panel');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            panels.forEach(p => p.classList.remove('active'));

            tab.classList.add('active');
            document.getElementById(tab.dataset.target).classList.add('active');
        });
    });

    // VIN Decode
    const vinForm = document.getElementById('vin-form');
    vinForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const vin = document.getElementById('vin-input').value;
        const btn = vinForm.querySelector('button');
        const resultDiv = document.getElementById('vin-result');
        const errorDiv = document.getElementById('vin-error');
        const grid = resultDiv.querySelector('.result-grid');

        setLoading(btn, true);
        resultDiv.style.display = 'none';
        errorDiv.style.display = 'none';

        try {
            const res = await fetch(`/api/vin/${vin}`);
            const data = await res.json();

            if (data.status === 'success') {
                grid.innerHTML = '';
                Object.entries(data.data).forEach(([key, value]) => {
                    grid.innerHTML += `
                        <div class="result-item">
                            <div class="result-label">${key}</div>
                            <div class="result-value">${value || 'N/A'}</div>
                        </div>
                    `;
                });
                resultDiv.style.display = 'block';
            } else {
                showError(errorDiv, data.message || 'Could not decode VIN');
            }
        } catch (err) {
            showError(errorDiv, 'Network error occurred');
        } finally {
            setLoading(btn, false);
        }
    });

    // Make/Model Lookup
    const makeSelect = document.getElementById('make-select');
    const yearInput = document.getElementById('year-input');
    const modelForm = document.getElementById('model-form');

    // Load Makes on init
    loadMakes();

    async function loadMakes() {
        try {
            const res = await fetch('/api/makes');
            const data = await res.json();
            if (data.status === 'success') {
                data.makes.sort().forEach(make => {
                    const option = document.createElement('option');
                    option.value = make;
                    option.textContent = make;
                    makeSelect.appendChild(option);
                });
            }
        } catch (err) {
            console.error('Failed to load makes', err);
        }
    }

    modelForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const make = makeSelect.value;
        const year = yearInput.value;
        const btn = modelForm.querySelector('button');
        const resultDiv = document.getElementById('model-result');
        const errorDiv = document.getElementById('model-error');
        const list = resultDiv.querySelector('.model-list');

        if (!make || !year) return;

        setLoading(btn, true);
        resultDiv.style.display = 'none';
        errorDiv.style.display = 'none';

        try {
            const res = await fetch(`/api/models/${make}/${year}`);
            const data = await res.json();

            if (data.status === 'success' && data.models.length > 0) {
                list.innerHTML = data.models.map(m =>
                    `<div class="result-item"><div class="result-value">${m}</div></div>`
                ).join('');
                resultDiv.style.display = 'block';
            } else {
                showError(errorDiv, 'No models found for this criteria');
            }
        } catch (err) {
            showError(errorDiv, 'Network error occurred');
        } finally {
            setLoading(btn, false);
        }
    });

    function setLoading(btn, isLoading) {
        if (isLoading) {
            const originalText = btn.innerText;
            btn.dataset.text = originalText;
            btn.innerHTML = '<span class="loader"></span> Processing...';
            btn.disabled = true;
        } else {
            btn.innerText = btn.dataset.text || 'Submit';
            btn.disabled = false;
        }
    }

    function showError(el, msg) {
        el.textContent = msg;
        el.style.display = 'block';
    }
});
