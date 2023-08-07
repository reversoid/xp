import { Injectable, NotImplementedException } from '@nestjs/common';
import { Tokens } from '../auth/auth.service';

@Injectable()
export class ProtectedService {
  /** Get auth tokens and renews it if necessary */
  async getTokensByTgUserId(
    userId: number,
    secretKey: string,
  ): Promise<Tokens> {
    throw new NotImplementedException({ userId, secretKey });
  }

  async getAllUnfinishedExperiments(): Promise<void> {
    throw new NotImplementedException();
  }
}
