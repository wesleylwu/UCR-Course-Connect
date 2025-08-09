import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.json({ message: "docker is easy" });
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
