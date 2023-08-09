import { CanActivate, ExecutionContext, Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Request } from 'express';
import { User } from 'src/modules/user/entities/user.entity';
import { Repository } from 'typeorm';

// TODO later extend Jwt Auth Guard, now it is useless because we have only telegram clients

@Injectable()
export class AuthGuard implements CanActivate {
  constructor(
    @InjectRepository(User) private userRepository: Repository<User>,
  ) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest() as Request;

    const tg_secret_key = request.headers['tg_secret_key'];
    const tg_user_id = request.headers['tg_user_id'];

    if (tg_secret_key === undefined || tg_user_id === undefined) {
      return false;
    }

    const numeric_tg_user_id = Number(tg_user_id);

    if (Number.isNaN(numeric_tg_user_id)) {
      return false;
    }

    const user = await this.userRepository.findOneBy({
      tg_id: numeric_tg_user_id,
    });

    request['user'] = user;

    return Boolean(user);
  }
}
