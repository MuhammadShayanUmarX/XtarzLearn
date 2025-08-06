// Smooth scroll for anchor links
const scrollLinks = document.querySelectorAll('a[href^="#"]');
scrollLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href').slice(1);
        const target = document.getElementById(targetId);
        if (target) {
            e.preventDefault();
            window.scrollTo({
                top: target.getBoundingClientRect().top + window.scrollY - 70,
                behavior: 'smooth'
            });
        }
    });
});

// Reveal feature cards on scroll
function revealCards() {
    const cards = document.querySelectorAll('.feature-card');
    const windowHeight = window.innerHeight;
    cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        if (cardTop < windowHeight - 60) {
            card.classList.add('visible');
        }
    });
}

// Initialize all event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize scroll reveal
    window.addEventListener('scroll', revealCards);
    revealCards();

    // Helper function to show/hide elements
    function setElementDisplay(id, show) {
        const el = document.getElementById(id);
        if (el) el.style.display = show ? 'block' : 'none';
    }

    // Helper function to handle API responses
    async function handleApiResponse(response, resultElementId) {
        if (!response.ok) {
            const errorText = await response.text();
            console.error('API Error:', errorText);
            throw new Error(`Server error: ${response.status}`);
        }
        
        const data = await response.json();
        if (data.error) {
            throw new Error(data.error);
        }
        
        const resultElement = document.getElementById(resultElementId);
        if (resultElement) {
            resultElement.innerHTML = data[Object.keys(data)[0]] || 'No data received';
            resultElement.style.display = 'block';
        }
        
        return data;
    }

    // Helper function to show error message
    function showError(error, errorElementId) {
        console.error('Error:', error);
        const errorMessage = error.message || 'An error occurred. Please try again.';
        const errorElement = document.getElementById(errorElementId);
        if (errorElement) {
            errorElement.textContent = errorMessage;
            errorElement.style.display = 'block';
        } else {
            alert(errorMessage);
        }
    }

    // Initialize all forms
    function initializeForms() {
        // Study Guide Form
        const studyGuideForm = document.getElementById('studyGuideForm');
        if (studyGuideForm) {
            studyGuideForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const topic = document.getElementById('guideTopic')?.value;
                const level = document.getElementById('guideLevel')?.value || 'intermediate';
                const focus = document.getElementById('guideFocus')?.value || '';
                
                setElementDisplay('guideLoading', true);
                setElementDisplay('guideResult', false);
                setElementDisplay('guideError', false);
                
                try {
                    const response = await fetch('/create_guide', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            topic: topic,
                            level: level,
                            focus_areas: focus
                        })
                    });
                    
                    await handleApiResponse(response, 'guideResult');
                } catch (error) {
                    showError(error, 'guideError');
                } finally {
                    setElementDisplay('guideLoading', false);
                }
            });
        }

        // Practice Questions Form
        const questionsForm = document.getElementById('questionsForm');
        if (questionsForm) {
            questionsForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const topic = document.getElementById('questionTopic')?.value;
                const numQuestions = document.getElementById('questionCount')?.value || 5;
                const questionTypesSelect = document.getElementById('questionTypes');
                const questionTypes = questionTypesSelect ? 
                    Array.from(questionTypesSelect.selectedOptions).map(option => option.value) : 
                    ['multiple_choice', 'true_false', 'short_answer'];
                
                setElementDisplay('questionsLoading', true);
                setElementDisplay('questionsResult', false);
                setElementDisplay('questionsError', false);
                
                try {
                    const response = await fetch('/generate_questions', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            topic: topic,
                            num_questions: parseInt(numQuestions),
                            question_types: questionTypes
                        })
                    });
                    
                    await handleApiResponse(response, 'questionsResult');
                } catch (error) {
                    showError(error, 'questionsError');
                } finally {
                    setElementDisplay('questionsLoading', false);
                }
            });
        }

        // Explain Topic Form
        const explainForm = document.getElementById('explainForm');
        if (explainForm) {
            explainForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const topic = document.getElementById('explainTopic')?.value;
                const level = document.getElementById('explainLevel')?.value || 'beginner';
                
                setElementDisplay('explainLoading', true);
                setElementDisplay('explainResult', false);
                setElementDisplay('explainError', false);
                
                try {
                    const response = await fetch('/explain_topic', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            topic: topic,
                            difficulty_level: level
                        })
                    });
                    
                    await handleApiResponse(response, 'explainResult');
                } catch (error) {
                    showError(error, 'explainError');
                } finally {
                    setElementDisplay('explainLoading', false);
                }
            });
        }

        // Summarize Form
        const summarizeForm = document.getElementById('summarizeForm');
        if (summarizeForm) {
            summarizeForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const text = document.getElementById('summarizeText')?.value;
                const summaryType = document.getElementById('summaryType')?.value || 'paragraph';
                
                setElementDisplay('summarizeLoading', true);
                setElementDisplay('summarizeResult', false);
                setElementDisplay('summarizeError', false);
                
                try {
                    const response = await fetch('/summarize_text', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            text: text,
                            summary_type: summaryType
                        })
                    });
                    
                    await handleApiResponse(response, 'summarizeResult');
                } catch (error) {
                    showError(error, 'summarizeError');
                } finally {
                    setElementDisplay('summarizeLoading', false);
                }
            });
        }
    }

    // Initialize all forms when the page loads
    initializeForms();
});
