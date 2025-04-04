document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('converter-form');
    const regexInput = document.getElementById('regex-input');
    const errorMessage = document.getElementById('error-message');
    const resultsSection = document.getElementById('results-section');
    
    // Form submission handler
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const regex = regexInput.value.trim();
        if (!regex) {
            showError('Please enter a regular expression');
            return;
        }
        
        try {
            // Show loading state
            form.querySelector('button').textContent = 'Processing...';
            form.querySelector('button').disabled = true;
            
            // Send request to server
            const response = await fetch('/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ regex: regex })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                displayResults(data);
            } else {
                showError(data.error || 'An error occurred');
            }
        } catch (error) {
            showError('Network error: ' + error.message);
        } finally {
            // Reset button state
            form.querySelector('button').textContent = 'Convert';
            form.querySelector('button').disabled = false;
        }
    });
    
    // Display results from server
    function displayResults(data) {
        // Update processing steps
        document.getElementById('input-regex').textContent = data.regex;
        document.getElementById('prepared-infix').textContent = data.prepared;
        document.getElementById('postfix-notation').textContent = data.postfix;
        
        // Update NFA description
        const nfaDesc = document.getElementById('nfa-description');
        nfaDesc.innerHTML = '';
        
        const initialP = document.createElement('p');
        initialP.innerHTML = `<strong>Initial State:</strong> ${data.nfa_description.initial}`;
        nfaDesc.appendChild(initialP);
        
        const acceptP = document.createElement('p');
        acceptP.innerHTML = `<strong>Accepting State:</strong> <span class="final-state">${data.nfa_description.accept}</span>`;
        nfaDesc.appendChild(acceptP);
        
        const transHeader = document.createElement('h4');
        transHeader.textContent = 'Transitions:';
        nfaDesc.appendChild(transHeader);
        
        const transList = document.createElement('div');
        transList.className = 'transitions-list';
        data.nfa_description.transitions.forEach(trans => {
            const transDiv = document.createElement('div');
            transDiv.className = 'transition';
            transDiv.innerHTML = `${trans.source} --${trans.label}--> ${trans.target}`;
            if (trans.is_final) {
                transDiv.innerHTML += '<span class="final-state"> (final state)</span>';
            }
            transList.appendChild(transDiv);
        });
        nfaDesc.appendChild(transList);
        
        // Update transition table
        const tableContainer = document.getElementById('transition-table');
        tableContainer.innerHTML = '';
        
        const table = document.createElement('table');
        const thead = document.createElement('thead');
        thead.innerHTML = `
            <tr>
                <th>State</th>
                <th>Symbol</th>
                <th>Next State(s)</th>
            </tr>
        `;
        table.appendChild(thead);
        
        const tbody = document.createElement('tbody');
        data.transition_table.forEach(row => {
            const tr = document.createElement('tr');
            
            const stateTd = document.createElement('td');
            stateTd.textContent = row.state;
            tr.appendChild(stateTd);
            
            const symbolTd = document.createElement('td');
            symbolTd.textContent = row.symbol;
            tr.appendChild(symbolTd);
            
            const nextTd = document.createElement('td');
            nextTd.innerHTML = row.next_states.map(state => {
                return `${state.id}${state.is_final ? '<span class="final-state"> (final)</span>' : ''}`;
            }).join(', ');
            tr.appendChild(nextTd);
            
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        tableContainer.appendChild(table);
        
        // Update graphs
        const nfaImgContainer = document.getElementById('nfa-graph-container');
        nfaImgContainer.innerHTML = '';
        const nfaImg = document.createElement('img');
        nfaImg.src = `/graphs/${data.nfa_image}`;
        nfaImg.alt = 'NFA Graph';
        nfaImgContainer.appendChild(nfaImg);
        
        const dfaImgContainer = document.getElementById('dfa-graph-container');
        dfaImgContainer.innerHTML = '';
        const dfaImg = document.createElement('img');
        dfaImg.src = `/graphs/${data.dfa_image}`;
        dfaImg.alt = 'DFA Graph';
        dfaImgContainer.appendChild(dfaImg);
        
        // Show results section
        resultsSection.classList.remove('hidden');
        resultsSection.scrollIntoView({ behavior: 'smooth' });
        
        // Clear any previous errors
        hideError();
    }
    
    // Error handling
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        resultsSection.classList.add('hidden');
    }
    
    function hideError() {
        errorMessage.style.display = 'none';
    }
});