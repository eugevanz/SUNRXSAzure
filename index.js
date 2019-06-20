const express = require("express");
const path = require("path");
const cors = require("cors");
const { spawn } = require("child_process");
const app = express();
const port = process.env.PORT || 1337;

app.use(cors());
app.use(express.static(path.join(__dirname, "dist")));

app.get("/SOAPIncidents", (req,res) => {
    const spawn = require("child_process").spawn;
    const process = spawn("python", ["./get_soap_data.py"]);

    process.stdout.on("data", data => {
        res.send(data);
    });
});

app.get("/FireIncidents", (req, res) => {
    const process = spawn("python", ["./get_fire_data.py"]);

    process.stdout.on("data", data => res.send(`data: ${data}`));
    process.stderr.on("data", data => console.log(`error: ${data}`));
    process.stderr.on("close", () => console.log("Closed"));
});

app.get("/FetchFire", (req,res) => {
    res.send("Use me, I'm empty");
})

app.get('*', (req,res) =>{
    res.sendFile(path.join(`${__dirname}/dist/index.html`));
});

app.listen(port, () => console.log(`Listening On PORT ${port}`));