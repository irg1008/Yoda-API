import { db } from 'lib/db';
import type { CreateUserData } from 'lib/db/models';
import { hash } from 'lib/utils/crypto';

const get = (id: string) => db.user.findUnique({ where: { id } });

const getByEmail = (email: string) => db.user.findUnique({ where: { email } });

const create = async (createData: CreateUserData) => {
  const user = await getByEmail(createData.email);
  if (user) throw new Error('User already exists');
  const data = { ...createData, password: hash(createData.password) };
  return db.user.create({ data });
};

export default {
  get,
  getByEmail,
  create,
};
