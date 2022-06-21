import { opine, json } from "opine";
import { User } from "/db/models/index.ts";

export const appUser = opine();
appUser.use(json());

appUser.get("/", async (req, res) => {
	try {
		const users = await User.all();
		res.json(users);
	} catch (error) {
		console.log(error);
		res.sendStatus(500).send({ error: "Oh shaaait" });
	}
});

appUser.get("/:id", async (req, res) => {
	try {
		const user = await User.find(req.params.id);
		if (!user) return res.sendStatus(404).send("User not found");
		res.json(user);
	} catch (error) {
		console.log(error);
		res.sendStatus(500).send({ error: "Oh shaaait" });
	}
});

appUser.post("/", async (req, res) => {
	try {
		const user = await User.create(req.body);
		res.json(user);
	} catch (error) {
		console.log(error);
		res.sendStatus(500).send({ error: "Oh shaaait" });
	}
});
