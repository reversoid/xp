import { User } from "../models/user.js";
import { UserRepository } from "../repositories/user.repository.js";

export class UserService {
  userRepository: UserRepository;

  constructor({ userRepository }: { userRepository: UserRepository }) {
    this.userRepository = userRepository;
  }

  async getUserByTgId(tgId: bigint): Promise<User | null> {
    return this.userRepository.getUserByTgId(tgId);
  }
}
