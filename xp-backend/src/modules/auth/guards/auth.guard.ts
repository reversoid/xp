import {
  CanActivate,
  ExecutionContext,
  Inject,
  Injectable,
} from '@nestjs/common';
import { ConfigType } from '@nestjs/config';
import { InjectRepository } from '@nestjs/typeorm';
import { Request } from 'express';
import secretsConfig from 'src/config/secrets.config';
import { UserRepository } from 'src/modules/user/repositories/user.repository';

// TODO later extend Jwt Auth Guard, now it is useless because we have only telegram clients

@Injectable()
export class AuthGuard implements CanActivate {
  constructor(
    @InjectRepository(UserRepository) private userRepository: UserRepository,
    @Inject(secretsConfig.KEY)
    private secrets: ConfigType<typeof secretsConfig>,
  ) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest() as Request;

    const secret_key = request.headers['secret_key'];
    const tg_user_id = request.headers['tg_user_id'];

    if (secret_key === undefined || tg_user_id === undefined) {
      return false;
    }

    const numeric_tg_user_id = Number(tg_user_id);

    if (Number.isNaN(numeric_tg_user_id)) {
      return false;
    }

    if (!this.secrets.apiSecretKeys.includes(String(secret_key))) {
      return false;
    }

    const user = await this.userRepository.findOneBy({
      tg_id: numeric_tg_user_id,
    });

    request['user'] = user;

    return Boolean(user);
  }
}
