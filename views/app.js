const loading = document.getElementById("loading");
const error = document.getElementById("error");
const dataList = document.getElementById("data-list");

async function loadData() {
    try {
        loading.style.display = "block";
        loading.textContent = "Loading data...";

        error.textContent = "";
        dataList.innerHTML = "";

        const response = await fetch(
            "http://127.0.0.1:5000/api/data"
        );

        if (!response.ok) {
            throw new Error("Server Error");
        }

        const result = await response.json();

        await new Promise(resolve => setTimeout(resolve, 2000));
        loading.style.display = "none";

        result.data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.id} - ${item.name}`;
            dataList.appendChild(li);
        });

    } catch (err) {
        loading.style.display = "none";
        error.textContent =
            "Gagal mengambil data dari backend";
    }
}

loadData();