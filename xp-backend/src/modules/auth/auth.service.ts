import {
  HttpException,
  Injectable,
  NotImplementedException,
} from '@nestjs/common';
import { RegisterDTO } from './dto/register.dto';
import { LoginDTO } from './dto/login.dto';
import { UserRepository } from '../user/repositories/user.repository';
import * as bcrypt from 'bcrypt';

export interface Tokens {
  access_token: string;
  refresh_token: string;
}

class UserExistsException extends HttpException {
  constructor() {
    super('USER_EXISTS', 400);
  }
}

@Injectable()
export class AuthService {
  constructor(private readonly userRepository: UserRepository) {}

  async register(dto: RegisterDTO): Promise<void> {
    await this.validateUserExistence(dto.username, dto.tg_user_id);

    const passwordHash = await bcrypt.hash(dto.password, 12);

    const newUser = this.userRepository.create({
      tg_id: dto.tg_user_id,
      username: dto.username,
      password_hash: passwordHash,
    });

    await this.userRepository.save(newUser);
  }

  async login(dto: LoginDTO): Promise<Tokens> {
    throw new NotImplementedException({ dto });
  }

  private async validateUserExistence(username: string, tgId?: number) {
    const userExists = await this.userRepository.findOneBy([
      { tg_id: tgId },
      { username: username },
    ]);

    if (userExists) {
      throw new UserExistsException();
    }
  }
}
