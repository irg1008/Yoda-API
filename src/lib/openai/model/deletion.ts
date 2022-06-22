import { withError } from '../utils/error-handler';
import { openai } from './api';

export const deleteModel = (model: string) => withError(() => openai.deleteModel(model));
