// Rock catalog data
const rocks = [
    {
        name: "Brown Rocks",
        hsv: {
            lower: { h: 10, s: 50, v: 50 },
            upper: { h: 25, s: 255, v: 255 }
        }
    },
    {
        name: "Gray Rocks",
        hsv: {
            lower: { h: 0, s: 0, v: 50 },
            upper: { h: 179, s: 50, v: 200 }
        }
    },
    {
        name: "Yellow Rocks",
        hsv: {
            lower: { h: 20, s: 100, v: 100 },
            upper: { h: 40, s: 255, v: 255 }
        }
    }
];

// Initialize rock catalog
document.addEventListener('DOMContentLoaded', () => {
    const catalogDiv = document.getElementById("rock-list");
    if (catalogDiv) {
        rocks.forEach(rock => {
            const rockDiv = document.createElement("div");
            rockDiv.className = "rock-item";
            
            rockDiv.innerHTML = `
                <h4>${rock.name}</h4>
                <div class="hsv-values">
                    <div>Lower: H(${rock.hsv.lower.h}), S(${rock.hsv.lower.s}), V(${rock.hsv.lower.v})</div>
                    <div>Upper: H(${rock.hsv.upper.h}), S(${rock.hsv.upper.s}), V(${rock.hsv.upper.v})</div>
                </div>
            `;
            
            catalogDiv.appendChild(rockDiv);
        });
    }
});

// Tour functionality
let currentStep = 0;
const steps = document.querySelectorAll('.step');
const modal = document.getElementById('onboarding-modal');

function showStep(index) {
    steps.forEach(step => step.classList.remove('active'));
    const current = steps[index];
    current.classList.add('active');
    
    const target = current.getAttribute('data-target');
    if(target) {
        document.querySelectorAll('.highlight').forEach(el => el.classList.remove('highlight'));
        document.querySelector(target).classList.add('highlight');
    }
    
    // Update progress indicator
    const progress = document.querySelector('.progress-indicator');
    if(progress) {
        progress.textContent = `Step ${currentStep + 1} of ${steps.length}`;
    }
}

function nextStep() {
    if(currentStep < steps.length - 1) {
        currentStep++;
        showStep(currentStep);
    }
}

function prevStep() {
    if(currentStep > 0) {
        currentStep--;
        showStep(currentStep);
    }
}

function closeTour() {
    modal.style.display = 'none';
    document.querySelectorAll('.highlight').forEach(el => el.classList.remove('highlight'));
    localStorage.setItem('tourCompleted', true);
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize tour
    if(!localStorage.getItem('tourCompleted')) {
        modal.style.display = 'block';
        showStep(0);
    }
    
    // Add progress indicator
    const progress = document.createElement('div');
    progress.className = 'progress-indicator';
    document.querySelector('.modal-content').appendChild(progress);
});