<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        h3 {
            margin-top: 20px;
            color: #333;
        }

        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 300px;
            overflow: hidden;
        }

        img {
            max-width: 100%;
            max-height: 100%;
            object-fit: cover;
            animation: fadeInOut 5s infinite;
        }

        button {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #0056b3;
        }

        @keyframes fadeInOut {
            0%, 100% {
                opacity: 0;
            }
            50% {
                opacity: 1;
            }
        }
    </style>
    <title>Banner</title>
</head>
<body>
    <h3>Welcomepicture</h3>
    <div class="image-container">
        <img id="bannerImage" src="" alt="Banner Image">
    </div>
    <script>
        const banners = ["b1.jpg", "b2.jpg", "b3.jpg", "b4.jpg", "b5.jpg"];
        const imageElement = document.getElementById("bannerImage");

        let i = 0;
        const interval = setInterval(() => {
            if (i === banners.length) {
                i = 0;
            }
            const imgSrc = banners[i];
            imageElement.src = imgSrc;
            i++;
        }, 3000);
    </script>
</body>
</html>