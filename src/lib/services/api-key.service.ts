import { db } from 'lib/db';

const create = async (name: string) => db.apiKey.create({ data: { name } });

const list = async () => db.apiKey.findMany();

const get = async (id: string) => db.apiKey.findUnique({ where: { id } });

const getByKey = async (key: string) =>
  db.apiKey.findUnique({ where: { apiKey: key } });

const remove = async (id: string) => {
  const apiKey = await get(id);
  if (!apiKey) return null;
  return db.apiKey.delete({ where: { id } });
};

export default {
  create,
  list,
  remove,
  get,
  getByKey,
};
