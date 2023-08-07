import { Injectable, NotImplementedException } from '@nestjs/common';
import { RegisterDTO } from './dto/register.dto';
import { LoginDTO } from './dto/login.dto';

export interface Tokens {
  access_token: string;
  refresh_token: string;
}

@Injectable()
export class AuthService {
  async getTokensByTgUserId(userId: number, apiKey: string): Promise<Tokens> {
    throw new NotImplementedException({ userId, apiKey });
  }

  async register(dto: RegisterDTO): Promise<Tokens> {
    throw new NotImplementedException({ dto });
  }

  async login(dto: LoginDTO): Promise<Tokens> {
    throw new NotImplementedException({ dto });
  }

  private async getTokensByUserId(userId: number): Promise<Tokens> {
    throw new NotImplementedException({ userId });
  }
}
