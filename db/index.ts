import { PostgresConnector, Database } from "denodb";
import models from "/db/models/index.ts";
import { config } from "dotenv";

interface ContextOptions {
	/**
	 * Use this when updating db schemas or adding new tables.
	 * Will reset all tables but there is no migrations or anty workaround yet.
	 * Will do for the moment.
	 * A way to use this without dropping all tables is to only pass the models we want to change to the link funciton.
	 * Then only them will be "dropped" if set.
	 * 
	 * Maybe the best option would be to change to postgres client:
	 * i.e.: https://deno.land/x/postgresjs@v3.2.4
	 *
	 * @type {boolean}
	 * @memberof ContextOptions
	 */
	reset: boolean;
}

const defaultOptions: ContextOptions = {
	reset: false,
};

const getDB = () => {
	const { DATABASE_URI } = config({ safe: true });

	const connection = new PostgresConnector({
		uri: DATABASE_URI,
	});

	return new Database(connection);
};

const linkModels = (db: Database) => db.link(models);
const syncDB = async (db: Database) => await db.sync({ drop: true });

const createContext = async ({ reset }: ContextOptions = defaultOptions) => {
	const db = getDB();
	linkModels(db);
	if (reset) await syncDB(db);
};

export { createContext };
