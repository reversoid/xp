import { ApiHeaderOptions } from '@nestjs/swagger';

export const AuthHeaders: ApiHeaderOptions[] = [
  { name: 'secret_key', description: 'API-KEY' },
  { name: 'tg_user_id', description: 'Telegram userID' }, // TODO when tg user_id will be not needed necessarily, mark option "allow empty value" as true
];
