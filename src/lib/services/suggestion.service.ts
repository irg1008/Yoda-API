import { db } from 'lib/db';
import type { SuggestionData } from 'lib/db/models';

const logSuggestion = (data: SuggestionData) => db.suggestion.create({ data });

export default {
  logSuggestion,
};
