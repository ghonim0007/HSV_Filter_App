// script.js
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

// Populate rock catalog
const catalogDiv = document.getElementById("rock-list");

rocks.forEach((rock) => {
    const rockDiv = document.createElement("div");
    rockDiv.className = "rock-item";

    rockDiv.innerHTML = `
        <h3>${rock.name}</h3>
        <p><strong>Lower HSV:</strong> H: ${rock.hsv.lower.h}, S: ${rock.hsv.lower.s}, V: ${rock.hsv.lower.v}</p>
        <p><strong>Upper HSV:</strong> H: ${rock.hsv.upper.h}, S: ${rock.hsv.upper.s}, V: ${rock.hsv.upper.v}</p>
    `;

    catalogDiv.appendChild(rockDiv);
});
