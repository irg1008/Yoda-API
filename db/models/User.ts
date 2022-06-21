import { DataTypes, Model } from "denodb";

const getRandomId = () => {
	return crypto.randomUUID();
};

export class User extends Model {
	static table = "users";
	static timestamps = true;

	static fields = {
		id: { type: DataTypes.STRING, primaryKey: true, },
		role: DataTypes.enum(["admin", "user"]),
	};

	static defaults = {
		id: getRandomId,
		role: "user",
	};
}
