import {
  CanActivate,
  ExecutionContext,
  Inject,
  Injectable,
} from '@nestjs/common';
import { ConfigType } from '@nestjs/config';
import { Request } from 'express';
import secretsConfig from 'src/config/secrets.config';

@Injectable()
export class ProtectedGuard implements CanActivate {
  constructor(
    @Inject(secretsConfig.KEY)
    private secrets: ConfigType<typeof secretsConfig>,
  ) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest() as Request;

    const secret_key = request.headers['secret_key'];

    if (secret_key === undefined) {
      return false;
    }

    if (!this.secrets.apiSecretKeys.includes(String(secret_key))) {
      return false;
    }

    return true;
  }
}
