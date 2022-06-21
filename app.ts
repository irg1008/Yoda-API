import { createContext } from "/db/index.ts";
import { opine } from "opine";
import { appUser } from "/router/index.ts";

createContext();

const app = opine();

app.get("/", (req, res) => {
	res.send("Hello World!");
});

app.use("/user", appUser);

const port = 5000;
app.listen(port);
console.log(`Listening on  https://localhost:${port}`);
